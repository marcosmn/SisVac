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
              :data="vacinacao.dados"
            >
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
const vacinacaoColumns = ["Data", "Vacina", "Estabelecimento", "Particular"];
const tableData = [
  {
    Data: 1,
    Vacina: "Dakota Rice",
    Estabelecimento: "$36.738",
    Particular: "Niger",
  },
  {
    Data: 2,
    Vacina: "dd Rice",
    Estabelecimento: "$36.dd738",
    Particular: "Niger",
  },
];
export default {
  components: {
    LTable,
    Card,
  },
  data() {
    return {
      vacinacao: {
        columns: [...vacinacaoColumns],
        dados: [...tableData],
      },
    };
  },
  mounted() {
    userService.getCarteira().then((dados) => {
        console.info(dados);
        this.vacinacao.dados = dados;
    });
  },
};
</script>
<style></style>
