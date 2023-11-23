import React from "react"
import { Link } from "react-router-dom"


const Login = () => {
    return (
        <>
            <div className="container mt-5">
                <div className="row justify-content-center">
                    <h2 className="text-center my-3">Ingresar a plataforma</h2>
                    <div className="col-12 col-md-6 border py-4">
                        <form>
                            <div className="form-group mb-3">
                                <label>Email:</label>
                                <input
                                    type="text"
                                    placeholder="elquefrao@email.com"
                                    className="form-control"
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label>Contraseña:</label>
                                <input
                                    type="password"
                                    placeholder="123456"
                                    className="form-control"
                                />
                            </div>
                            <button className=" btn btn-outline-primary w-100">Iniciar sesión</button>
                        </form>

                    </div>
                    <div className="w-100"></div>

                    <div className="col-12 col-md-6 d-flex justify-content-between my-1">
                        <Link to={`/register`}>Registrarme</Link>
                        <Link to={`/reset-password`}>Olvido su contraseña</Link>
                    </div>
                </div>
            </div>

        </>
    )
}

export default Login