import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	const probarSendEmail=async()=>{
		let response = await fetch(`${process.env.BACKEND_URL}/sendemail`, {
			method:"POST",
			headers:{
				"Content-Type":"application/json"
			},
			body:JSON.stringify({
				"subject": "Recuperar password",
				"to":"ropamera@gmail.com",
				"message":"Ingresa en este lin para recuperar la password"
			})
		})

		console.log(response)
	}

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			<p>
				<img src={rigoImageUrl} />
			</p>
			<div className="alert alert-info">
				{store.message || "Loading message from the backend (make sure your python backend is running)..."}
			</div>
			<p>
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://start.4geeksacademy.com/starters/react-flask">
					Read documentation
				</a>
			</p>

			<button onClick={()=>probarSendEmail()}>Probar endpoint</button>
		</div>
	);
};
