import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";

const ResetPass = () => {

    const { actions } = useContext(Context)

    const [email, setEmail] = useState("")

    const handleChange = (event) => {
        setEmail(event.target.value)
    }


    const handleSubmit = (event) => {
        event.preventDefault()
        actions.resetPassword(email)
    }

    return (
        <>
            <div className="container mt-5">
                <div className="row justify-content-center">
                    <h2 className="text-center my-3">Recuperar Contraseña</h2>
                    <div className="col-12 col-md-6 border py-4">
                        <form onSubmit={handleSubmit} >
                            <div className="form-group mb-3">
                                <label>Email:</label>
                                <input
                                    type="text"
                                    placeholder="elquefrao@email.com"
                                    className="form-control"
                                    name="email"
                                    value={email}
                                    onChange={handleChange}
                                />
                            </div>

                            <button className=" btn btn-outline-primary w-100">Enviar</button>
                        </form>

                    </div>
                    <div className="w-100"></div>

                    {/* <div className="col-12 col-md-6 d-flex justify-content-between my-1">
                        <Link to={`/register`}>Registrarme</Link>
                        <Link to={`/recuperar-contrasenia`}>Olvido su contraseña</Link>
                    </div> */}
                </div>
            </div>
        </>
    )
}


export default ResetPass