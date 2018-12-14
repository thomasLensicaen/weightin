from flask import Flask, request, redirect, jsonify, Response, send_file
import os
import sys
from werkzeug.utils import secure_filename
import pathlib
from config import Config
from apps.weightin import WeightInApp
from common.logtool import create_logger
from common.constant import data_post_field
import copy

app = Flask(__name__)

apps_map = None

def get_obj_from_form(result):
    return result[data_post_field] 


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
    return res 

@app.route("/get_data", methods=["POST"])
def get_data():
    result = request.form
    application_name = result['application_name']
    application = apps_map[application_name]
    res = application.get_data()
    return res

@app.route("/get_plot", methods=["POST"])
def get_plot():
    result = request.form
    application_name = result['application_name']
    application = apps_map[application_name]
    obj = request.args.get('obj')
    return res 

@app.route("/delete_data", methods=["POST"])
def delete_data():
    result = request.form
    application_name = result['application_name']
    obj = json.loads(get_obj_from_form(result))
    application = apps_map[application_name]
    obj = application.to_object(obj)
    res = application.delete_data(obj)
    return res 

@app.route("/delete_by_date", methods=["POST"])
def delete_by_date():
    result = request.form
    application_name = result['application_name']
    obj = get_obj_from_form(result)
    application = apps_map[application_name]
    res = application.delete_by_date(obj)
    return res 

if __name__ == '__main__':
    config_path = sys.argv[1]
    local_dir = pathlib.Path(__file__).resolve().parent
    cfg = Config.from_file(config_path)
    apps_map = {WeightInApp.name: WeightInApp(cfg.db_config)}
    logger = create_logger(cfg.log_config.filepath, cfg.log_config.level)
    app.run(host=cfg.app_config.host, port=cfg.app_config.port, debug=True)

