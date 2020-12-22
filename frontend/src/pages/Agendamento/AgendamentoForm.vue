<template>
  <card>
    <h4 slot="header" class="card-title">Agendamento de Vacina</h4>
    <form>
      <div class="row">
        <div class="col-md-12">
          <div class="form-group">
            <label for="vacina" class="control-label">Vacina</label>
            <select
              class="form-control"
              id="exampleFormControlSelect1"
              v-model="vacinaSelecionada"
              v-on:select="selectVacina"
            >
              <option
                v-for="vacina in vacinas"
                :key="vacina.vacina_id"
                v-bind:value="vacina.vacina_id"
              >
                {{ vacina.sigla + " - " + vacina.descricao }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-4">
          <div class="form-group">
            <label for="estado" class="control-label">Estado</label>
            <select
              class="form-control"
              id="exampleFormControlSelect1"
              v-model="estadoSelecionado"
              @change="selectEstado"
            >
              <option 
                v-for="estado in estados"
                :key="estado.uf"
                v-bind:value="estado.uf"
              >
                {{ estado.nome_uf }}
              </option>
            </select>
          </div>
        </div>
        <div class="col-md-8">
          <div class="form-group">
            <label for="municipio" class="control-label">Municipio</label>
            <select
              class="form-control"
              id="exampleFormControlSelect1"
              v-model="municipioSelecionado"
              @change="selectMunicipio"
            >
              <option
                v-for="municipio in municipios"
                :key="municipio.codigo_municipio"
                v-bind:value="municipio.codigo_municipio"
              >
                {{ municipio.nome_municipio }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <div class="form-group">
            <label for="estabelecimento" class="control-label">Estabelecimento</label>
            <select
              class="form-control"
              id="exampleFormControlSelect1"
              v-model="estabelecimentoSelecionado"
              @change="selectEstabelecimento"
            >
              <option
                v-for="estabelecimento in estabelecimentos"
                :key="estabelecimento.co_unidade"
                v-bind:value="estabelecimento.co_unidade"
              >
                {{ estabelecimento.no_fantasia }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <div class="form-group">
            <label for="agenda" class="control-label">Agenda</label>
            <select
              class="form-control"
              id="exampleFormControlSelect1"
              v-model="agendaSelecionada"
              @change="selectAgenda"
            >
              <option
                v-for="item in agenda"
                :key="item.agenda_id"
                v-bind:value="item.agenda_id"
              >
                {{ item.data_agendamento + ' às ' + item.hora }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="text-center">
        <button
          type="submit"
          class="btn btn-info btn-fill float-right"
          @click.prevent="agendarVacina"
        >
          Agendar
        </button>
      </div>
      <div class="clearfix"></div>
    </form>
  </card>
</template>
<script>
import Card from "src/components/Cards/Card.vue";
import vacinacaoService from "@/services/vacinacaoService";

export default {
  components: {
    Card,
  },
  data() {
    return {
      vacinaSelecionada: {},
      estadoSelecionado: {},
      agendaSelecionada: {},
      municipioSelecionado: {},
      estabelecimentoSelecionado: {},
      vacinas: [],
      estados: [],
      municipios: [],
      estabelecimentos: [],
      agenda: [],
      solicitacao: {
        data: "",
        hora: "",
        vacina: "",
        estabelecimento: "",
      },
    };
  },
  mounted() {
    vacinacaoService.getVacinas().then((dados) => {
      console.info(dados);
      this.vacinas = dados;
    });
    vacinacaoService.getEstados().then((dados) => {
      console.info(dados);
      this.estados = dados;
    });
  },
  methods: {
    agendarVacina() {
      console.info(this.vacinaSelecionada);
      //vacinaService.salvarDados(this.user);
    },
    selectVacina() {
      console.info(this.vacinaSelecionada);
      //vacinaService.salvarDados(this.user);
    },
    selectAgenda() {
      console.info(this.agendaSelecionada);
      //vacinaService.salvarDados(this.user);
    },
    selectMunicipio() {
      console.info(this.municipioSelecionado);
       vacinacaoService
        .getEstabelecimentos(this.municipioSelecionado)
        .then((dados) => {
          console.info(dados);
          this.estabelecimentos = dados;
        });
    },
    selectEstado() {
      console.info(this.estadoSelecionado);
      vacinacaoService
        .getMunicipios(this.estadoSelecionado)
        .then((dados) => {
          console.info(dados);
          this.municipios = dados;
        });
    },
    selectEstabelecimento() {
      console.info(this.estabelecimentoSelecionado);
      vacinacaoService
        .getAgenda(this.estabelecimentoSelecionado)
        .then((dados) => {
          console.info(dados);
          this.agenda = dados;
        });
    },
  },
};
</script>
<style></style>
