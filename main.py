from flask import Flask, request, redirect, jsonify, Response, send_file
import os
import sys
from werkzeug.utils import secure_filename
import pathlib
from config import Config
from apps.weightin import WeightInApp
from common.logtool import create_logger
import copy

app = Flask(__name__)

apps_map = None

def get_obj_from_form(result):
    raw = dict(copy.deepcopy(result))
    del raw['application_name']
    return raw


@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/add_data", methods=["POST"])
def add_data():
    result = request.form
    application_name = result['application_name']
    obj = get_obj_from_form(result)
    application = apps_map[application_name]
    obj = application.to_object(obj)
    res = application.add_data(obj)
    return "OK {}".format(res)

@app.route("/get_plot", methods=["POST"])
def get_plot():
    result = request.form
    application_name = result['application_name']
    application = apps_map[application_name]
    obj = request.args.get('obj')
    return ""

@app.route("/delete_data", methods=["POST"])
def delete_data():
    result = request.form
    application_name = result['application_name']
    application = apps_map[application_name]
    obj = request.args.get('obj')
    return ""

if __name__ == '__main__':
    config_path = sys.argv[1]
    local_dir = pathlib.Path(__file__).resolve().parent
    cfg = Config.from_file(config_path)
    apps_map = {WeightInApp.name: WeightInApp(cfg.db_config)}
    logger = create_logger(cfg.log_config.filepath, cfg.log_config.level)
    app.run(host=cfg.app_config.host, port=cfg.app_config.port, debug=True)

