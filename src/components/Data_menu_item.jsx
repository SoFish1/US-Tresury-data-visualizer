import React from 'react'

const Data_menu_item = ({data_field,setGraphJSON,set_y_GraphJSON,active_tab, setLoading}) => {
    const token = localStorage.getItem("token");
    


    const handleClick = () => {
        const opts = {
            method: "POST",
            headers: {
                
                "Authorization": `Bearer ${token}`,
                "Content-Type":"application/json"                
            },
            body: JSON.stringify(
                {
                    "field":data_field,
                    "tag":active_tab
                }
            )
        }

        fetch("/backend/main/get_data_plot",opts)
        .then(resp => {
            if(resp.status === 200) 
            {
                return resp.json();
                
            }
            else alert("Error to process!!")
            
        })
        .then((data) => {            
            setGraphJSON(JSON.parse(data.graph))
            set_y_GraphJSON(JSON.parse(data.y_graph))
            setLoading(false)
        })
        .catch(error => {
            console.log(error)
        })
 
    }



    return (
        
            <li class="list-group-item"   onClick={handleClick} >{data_field}</li>
        
    )
}

export default Data_menu_item
