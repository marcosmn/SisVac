import api from '@/services/api'

export default {
    verficaLogin() {
        return api.get('currentuser')
            .then(response => response.data)
    },
    logout() {
        return api.get('currentuser/logout')
            .then(response => response.data)
    },
    getDados() {
        return api.get('currentuser/dados')
            .then(response => response.data)
    },
    salvarDados(dados) {
        return api.put('currentuser/dados', dados)
            .then(response => response.data)
    },
    getCarteira() {
        return api.get('carteira')
            .then(response => response.data)
    }
}