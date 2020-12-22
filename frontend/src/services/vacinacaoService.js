import api from '@/services/api'

export default {
    getVacinas() {
        return api.get('vacina')
            .then(response => response.data)
    },
    getEstados() {
        return api.get('estado')
            .then(response => response.data)
    },
    getMunicipios(estado) {
        return api.get('municipio?estado='+estado)
            .then(response => response.data)
    },
    getEstabelecimentos(municipio) {
        return api.get('estabelecimento?municipio='+municipio)
            .then(response => response.data)
    },
    getAgenda(estabelecimento) {
        return api.get('agenda?estabelecimento='+estabelecimento)
            .then(response => response.data)
    },
    salvarAgenda(dados) {
        return api.post('agendamento', dados)
            .then(response => response.data)
    }

}