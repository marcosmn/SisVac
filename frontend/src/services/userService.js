import api from '@/services/api'

export default {
    verficaLogin() {
        return api.get('currentuser')
            .then(response => response.data)
    }
}