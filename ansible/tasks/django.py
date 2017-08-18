---
# vim:ff=unix ts=2 sw=2 ai expandtab
- name: git clone
  git:
    repo: "{{ git_repo }}"
    version: "{{ git_branch }}"
    dest: "{{ deploy_path }}"
    force: yes
    accept_hostkey: yes

- name: create virtualenv with requirements
  pip:
    virtualenv_python: python3
    virtualenv: "{{ env_root }}"
    requirements: "{{ deploy_path }}/requirements.txt"

- name: django migrate
  django_manage:
    command: migrate --fake-initial
    app_path: "{{ deploy_path }}"
    settings: "{{ django_settings_module }}"
    virtualenv: "{{ env_root }}"

- name: django collectstatic
  django_manage:
    command: collectstatic --no-input
    app_path: "{{ deploy_path }}"
    settings: "{{ django_settings_module }}"
    virtualenv: "{{ env_root }}"

- name: django loaddata
  django_manage:
    command: loaddata
    fixtures: "{{ django_initial_fixtures }}"
    app_path: "{{ deploy_path }}"
    settings: "{{ django_settings_module }}"
    virtualenv: "{{ env_root }}"

- name: chown home
  become: true
  file:
    state: directory
    recurse: yes
    path: "{{ home }}"
    owner: "{{ user }}"
    group: "{{ user }}"

- name: render supervisor conf
  become: true
  template:
    src: "../templates/supervisor_app.conf"
    dest: "/etc/supervisor/conf.d/{{ site_instance_name }}.conf"
  notify:
  - supervisorctl update

- name: render nginx conf
  become: true
  template:
    src: "../templates/nginx_gunicorn.conf"
    dest: "/etc/nginx/conf.d/{{ site_instance_name }}.conf"
  notify:
  - restart nginx service
