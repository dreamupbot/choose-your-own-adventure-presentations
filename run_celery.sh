#!/bin/bash
celery worker -l info -P gevent -A deploy_api.celery
