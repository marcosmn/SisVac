import userService from '../../services/userService'

const state = {
    email: "",
    logado: false,
    nome: "",
    grupos: []
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
            .then((dados) => {
                commit('setLogado',dados.logado)
                if(dados.logado) {
                    commit('atualizaDados', dados)
                } 
                console.info(dados)
            })
    },
    logout({state, commit}) {
        console.info("Saindo..")
        userService.logout()
            .then((dados) => {
                if(!dados.logado) {
                    location.reload(true);
                }
            })
    }
}

const mutations = {
    setLogado(state, estado) {
        state.logado = estado
    },
    atualizaDados(state, dados) {
        state.email = dados.email
        state.nome = dados.username
        state.grupos = dados.grupos
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}