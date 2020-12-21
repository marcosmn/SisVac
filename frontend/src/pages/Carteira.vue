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
            <!--
            <ul id="teste">
              <li v-for="value in vacinacao.data" :key="value.count">
                {{ value }}
              </li>
            </ul>
            -->
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

const vacinacaoColumns = ['Data_Vacinacao', 'Vacina', 'Estabelecimento', 'Privada']
  const tableData = []

export default {
  components: {
    LTable,
    Card,
  },
  data() {
    return {
      vacinacao: {
          columns: [...vacinacaoColumns],
          //data: []
          data: [...tableData]
        }
    }
  },
  mounted() {
    userService.getCarteira().then((dados) => {
      console.info(dados);
      this.vacinacao.data = dados.results;
    });
  },
};
/*
export default {
  el: '#teste',
  data() {
    return {
      vacinacao: [],
    };
  },
  mounted() {
    userService.getCarteira().then((dados) => {
      console.info(dados);
      this.data.vacinacao = dados;
    });
  },
}
*/
</script>
<style></style>
