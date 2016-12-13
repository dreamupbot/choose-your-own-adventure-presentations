#!/bin/bash
celery beat -A deploy_api.celery
