import React, { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Navbar from './components/Navbar';
import Login from './components/Login';
import Register from './components/Register';
import Confirmed_account from './components/Confirmed_account';
import Show_data from './components/Show_data';



function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [validate_email_token, setValidate_email_token] = useState("");
  
  useEffect(() =>{ 
    const token=localStorage.getItem("token")
    if(token){
      setIsAuthenticated(true)
    }
  }, [])


  
  return (
    <>
    <Router>
      <div className="App">
        <Navbar logged_status={isAuthenticated} logout_set={setIsAuthenticated}/>
        <Route 
          path='/login'
          render={() => ( <Login logged_status={isAuthenticated} sign_in={setIsAuthenticated}/>)}
           />
 
        <Route 
          path='/register'
          render={() => ( <Register grab_token={setValidate_email_token}/>)}
           />

        <Route 
          path={'/confirmed_account/' +  validate_email_token} 
          render={() => ( <Confirmed_account  />)}
           />
        
        
        <Route path='/show_data' 
        render={() => ( <Show_data  />)}
        />
      
      </div>


      

    </Router>

    
    </>
  );
}

export default App;
