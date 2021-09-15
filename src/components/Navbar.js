import React, { useEffect } from 'react'
import { Link } from 'react-router-dom'




const Navbar = (props) => {



    const Logout = () => {
        props.logout_set(false)
        localStorage.removeItem("token");
    }



    return (
        <>
        
                
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <div className="container-fluid">
                        
                        <Link className="navbar-brand" to="/show_data">US Financial data </Link>
                        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarNav">
                            <ul className="navbar-nav">

                            {(props.logged_status) ? (
                                <li className="nav-item">
                                    <Link to='/' className="nav-link"  onClick= {Logout}>Logout</Link>
                                </li>
                                ) : (

                                    <>
                                    <li className="nav-item">
                                        <Link to='/login' className="nav-link">Login</Link>
                                    </li>
                                    <li className="nav-item">
                                        <Link to='/register' className="nav-link">Register</Link>
                                    </li>
                                    </>
                                )}
                                
                            </ul>
                        </div>
                    </div>
                </nav>

        </>        
    )
}

export default Navbar
