const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			token: localStorage.getItem("token") || null
		},
		actions: {

		}
	};
};

export default getState;
