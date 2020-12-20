import userService from '../../services/userService'

const state = {
    logado: false,
    nome: ""
}

const getters = {
    logado: state => {
        return state.logado
    },
    nome: state => {
        return state.nome
    }
}

const actions = {
    getStatus({ state, commit }) {
        userService.verficaLogin()
            .then((estado) => {
                console.info("Estado:");
                console.info(estado)
            })
    },
}

const mutations = {
    setLogado(state, estado) {
        state.logado = estado
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}