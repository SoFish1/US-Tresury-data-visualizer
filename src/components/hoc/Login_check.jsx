import { useState, useEffect } from "react"
import { Redirect } from "react-router-dom"

const Login_check = (Component) => (props) => {
    
    const token = localStorage.getItem("token")

    if (token){
      return(<Component {...props} />)  
    }else{
        return(<Redirect to= '/login' />)
    }
    

}

export default Login_check
