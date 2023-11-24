import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Login from "../component/Login.jsx";
import { Navigate } from "react-router-dom"

import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);




	return (
		<>
			{
				store.token ?
					<h1>Tienes acceso</h1> :
					<Navigate to={"/login"} />
			}
		</>
	);
};
