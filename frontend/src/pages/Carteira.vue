<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <card
            class="strpied-tabled-with-hover"
            body-classes="table-full-width table-responsive"
          >
            <template slot="header">
              <h4 class="card-title">Posição na fila</h4>
              <p class="card-category">Andamento da sua solicitação</p>
            </template>
            <l-table
              class="table-hover table-striped"
              :columns="vacinacao.columns"
              :data="vacinacao.data">           
            </l-table>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import LTable from "src/components/Table.vue";
import Card from "src/components/Cards/Card.vue";
import userService from "@/services/userService";
const vacinacaoColumns = ['Id','Vacina', 'Data', 'Hora', 'Posição', 'Chamado']
  const tableData = [{
    id: 1,
    vacina: '',
    data: '',
    hora: '',
    posição: '',
    chamado: ''
  },
  {
    id: 2,
    vacina: '',
    data: '',
    hora: '',
    posição: '',
    chamado: ''
  },
  {
    id: 3,
    vacina: '',
    data: 'ddd',
    hora: '',
    posição: '',
    chamado: ''
  }
  ]
export default {
  components: {
    LTable,
    Card,
  },
  data() {
    return {
      vacinacao: {
          columns: [...vacinacaoColumns],
          data: [...tableData]
        }
    }
  }
  /*,
  /
  mounted() {
    userService.getCarteira().then((dados) => {
      //  console.info(dados);
      //  this.vacinacao.dados = dados;
    });
  },
  */
};
</script>
<style></style>
