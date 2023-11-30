const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			token: localStorage.getItem("token") || null
		},
		actions: {
			saveUser: async (user) => {
				const store = getStore()

				try {
					let response = await fetch(`${process.env.BACKEND_URL}/register`, {
						method: "POST",
						body: user
					})

					console.log(response)

				} catch (error) {
					console.log("error" + error)
				}
			},
			login: async (data) => {
				let store = getStore()
				try {
					let response = await fetch(`${process.env.BACKEND_URL}/login`, {
						method: "POST",
						headers: {
							"Content-Type": "application/json"
						},
						body: JSON.stringify(data)
					})

					if (response.ok) {
						let result = await response.json()
						console.log(result)
						setStore({
							token: result.token
						})
						localStorage.setItem("token", result.token)
					}
					return response.status

				} catch (error) {
					console.log(error)
				}
			},
			logout: () => {
				setStore({
					token: null
				})
				localStorage.removeItem("token")
			},
			resetPassword: async (email) => {
				const store = getStore()

				try {
					let response = await fetch(`${process.env.BACKEND_URL}/reset-password`, {
						method: "POST",
						headers: {
							"Content-Type": "application/json"
						},
						body: JSON.stringify(email)
					})

					console.log(response)
				} catch (error) {
					console.log(error)
				}
			}
		}
	};
};

export default getState;
