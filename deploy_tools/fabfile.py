#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Marvin King
# Date     : 2019-02-21 
from fabric.api import env, local, run
from fabric.contrib.files import append, exists, sed
import random

REPO_URL = 'https://github.com/king9sky/TDD_django.git'

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'source', 'virtualenv'):
        run(f'mkdir -p {site_folder}/{subfolder}')  # 使用-p会创建必要的目录（上级目录不存在会创建），目录已存在不会报错


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):  # 如果存在。git目录
        run(f'cd {source_folder} && git fetch')
        current_commit = local('git log -n 1 --format=%H', capture=True)
        run(f'cd {source_folder} && git reset --hard {current_commit}')  # 强制覆盖本地改动
    else:
        run(f'git clone {REPO_URL} {source_folder}')


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/TDDweb/settings.py'
    sed(settings_path, 'DEBUG = True', 'DEBUG = Flase')
    sed(settings_path,
        'ALLOWED_HOSTS =.$',
        f'ALLOWED_HOSTS = ["{site_name}"]')  # 正则匹配
    secret_key_file = source_folder + '/TDDweb/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(_+-=)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')


def _update_static_files(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py collectstatic --noinput'
    )


def _update_database(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py migrate --noinput'
    )


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)



