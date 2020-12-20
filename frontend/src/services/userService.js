import api from '@/services/api'

export default {
    verficaLogin() {
        return api.get('currentuser')
            .then(response => response.data)
    },
    logout() {
        return api.get('currentuser/logout')
            .then(response => response.data)
    }
}