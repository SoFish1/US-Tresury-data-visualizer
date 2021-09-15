import React from 'react'
import Data_menu_item from './Data_menu_item'
import { useState } from 'react'


const Data_menu = ({deposit_list,withdrawals_list, setGraphJSON, set_y_GraphJSON, setLoading}) => {
    const [active_tab, setActive_tab] = useState("Deposits");
    

    var MenuStyle = {
        maxHeight: "800px",
        overflowY: "scroll"
    };

    
    if(active_tab === "Deposits"){
        return <> 
            <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" value={active_tab} onClick={() => setActive_tab("Deposits")}>Deposits</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" value={active_tab}  onClick={() => setActive_tab("Withdrawals")}>Withdrawals</a>
            </li>
            </ul>
            
            <div class="col-md-4 " style={MenuStyle} >
                <ul className="nav flex-column "   >
                    { (deposit_list).map((x) =>  <Data_menu_item data_field={x} setGraphJSON={setGraphJSON} set_y_GraphJSON={set_y_GraphJSON} active_tab={active_tab} setLoading={setLoading}/>)}      
                </ul>
            </div>
        
        </>
    }else if (active_tab === "Withdrawals"){
        return <> 
        <ul class="nav nav-tabs">
        <li class="nav-item">
            <a class="nav-link " value={active_tab}  onClick={() => setActive_tab("Deposits")}>Deposits</a>
        </li>
        <li class="nav-item">
            <a class="nav-link active" value={active_tab}  onClick={() => setActive_tab("Withdrawals")}>Withdrawals</a>
        </li>
        </ul>
        <div class="col-md-4 " style={MenuStyle} >
            <ul className="nav flex-column "   >
                { (withdrawals_list).map((x) =>  <Data_menu_item data_field={x} setGraphJSON={setGraphJSON} set_y_GraphJSON={set_y_GraphJSON} active_tab={active_tab} setLoading={setLoading}/>)}      
            </ul>
        </div>
        </>
    }


   
}

export default Data_menu