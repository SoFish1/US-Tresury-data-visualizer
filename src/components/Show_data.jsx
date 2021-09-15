import { isArray } from 'lodash';
import { useEffect,useState } from 'react'
import Plot from 'react-plotly.js';
import Data_menu from './Data_menu';
import Login_check from './hoc/Login_check';
import Loader from "react-loader-spinner";
import fetchIntercept from 'fetch-intercept';

import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";



const Show_data = () => {
    const token = localStorage.getItem("token");
    const [deposit_list, setDeposit_list] = useState([]);
    const [withdrawals_list, setWithdrawals_list] = useState([]);
    const [graphJSON , setGraphJSON ] = useState({});
    const [y_graphJSON , set_y_GraphJSON ] = useState({});
    const [loading, setLoading] = useState(false)


    

    useEffect(() => {
        
        const opts = {
            method: "GET",
            headers: {
                
                "Authorization": `Bearer ${token}`,
                "Content-Type":"application/json"                
            }            
        }
        
            fetch("/backend/main/show_data",opts)
            .then(resp => {
                if(resp.status === 200) 
                {
                    
                    return resp.json();
                    
                }
                else alert("Error to process!!")
                
            })
            .then(data => {
                
                setDeposit_list(data.deposits)
                setWithdrawals_list(data.withdrawals)
                setGraphJSON(JSON.parse(data.default_graph))
                set_y_GraphJSON(JSON.parse(data.default_y_graph))
                setLoading(false)
                
            }).catch((error) => {
    
                console.log(error)
            });
            
        }
    


      ,[]);



      const unregister = fetchIntercept.register({
          request: function (url, config) {
              setLoading(true)
              // Modify the url or config here
              return [url, config];
          },
      
          requestError: function (error) {
              // Called when an error occured during another 'request' interceptor call
              return Promise.reject(error);
          },
      
          response:  function (response) {
              // Modify the reponse object
                            
              
              return response;
              
          },
      
          responseError: function (error) {
              // Handle an fetch error
              return Promise.reject(error);
          }
      });


    if(loading){ 
        return(<Loader
            type="Bars"
            color="#00BFFF"
            height={100}
            width={100}
            // timeout={3000} //3 secs
            style={{
                position: 'absolute', left: '50%', top: '50%',
                transform: 'translate(-50%, -50%)'
              }}
          />)
    }else{  

    return (
        
        <>
            <div className="container mt-2" >
                <div className="row">
                <Data_menu deposit_list={deposit_list} withdrawals_list={withdrawals_list} setGraphJSON={setGraphJSON} set_y_GraphJSON={set_y_GraphJSON} setLoading={setLoading}/>
                <div className="col-md-8 " >
                    <div className="row">
                    <Plot data={graphJSON.data} layout={graphJSON.layout} />
                    </div>
                    <div className="row">
                    <Plot data={y_graphJSON.data} layout={y_graphJSON.layout} />
                    </div>

                </div>
                </div>
            </div>
            
        </>
   
    )}
}

export default Login_check(Show_data)
