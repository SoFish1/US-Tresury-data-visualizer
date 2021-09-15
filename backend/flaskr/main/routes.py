from . import main_bp 
from flask import (request, g, redirect, current_app,jsonify)
from .data_plot import build_plot
from .build_query import build_query, get_last_fields
from flask_jwt_extended import jwt_required


@main_bp.route('/show_data', methods=['GET'])
@jwt_required()
def show_data():

    deposits=get_last_fields("Deposits")
    deposits=[field for field in deposits if "y_" not in field]
   
    withdrawals=get_last_fields("Withdrawals")
    withdrawals=[field for field in withdrawals if "y_" not in field]

    graphJSON = build_plot("Total Deposits (excluding transfers)",tag="Deposits",time_opt="")
    y_graphJSON = build_plot("Total Deposits (excluding transfers)",tag="Deposits",time_opt="y")

    data_load_page={"deposits":deposits,"withdrawals":withdrawals, "default_graph":graphJSON, "default_y_graph":y_graphJSON}

    return jsonify(data_load_page), 200
    

@main_bp.route('/get_data_plot', methods=['POST'])
@jwt_required()
def get_data_plot():

    field = request.json.get("field", None)
    tag = request.json.get("tag", None)

    

    graphJSON = build_plot(field=field,tag=tag,time_opt="")
    y_graphJSON = build_plot(field=field,tag=tag,time_opt="y")

    return jsonify({"graph":graphJSON,"y_graph":y_graphJSON }), 200

