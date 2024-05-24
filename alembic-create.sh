#!/bin/bash

alembic revision --rev-id "`date +'%Y_%m_%d__%H_%M_%S'`" -m "$1"