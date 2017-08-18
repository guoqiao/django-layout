---
# vim:ff=unix ts=2 sw=2 ai expandtab
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
