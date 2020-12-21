<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <card class="strpied-tabled-with-hover"
                body-classes="table-full-width table-responsive"
          >
            <template slot="header">
              <h4 class="card-title">Posição na fila</h4>
              <p class="card-category">Andamento da sua solicitação</p>
            </template>
            <l-table class="table-hover table-striped"
                     :columns="table1.columns"
                     :data="table1.data">
            </l-table>
          </card>

        </div>
  
      </div>
    </div>
  </div>
</template>
<script>
  import LTable from 'src/components/Table.vue'
  import Card from 'src/components/Cards/Card.vue'
  const tableColumns = ['Id','Vacina', 'Data', 'Hora', 'Posição', 'Chamado']
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
    data: '',
    hora: '',
    posição: '',
    chamado: ''
  },
  {
    id: 4,
    vacina: '',
    data: '',
    hora: '',
    posição: '',
    chamado: ''
  },
  {
    id: 5,
    vacina: '',
    data: '',
    hora: '',
    posição: '',
    chamado: ''
  }]
  export default {
    components: {
      LTable,
      Card
    },
    data () {
      return {
        table1: {
          columns: [...tableColumns],
          data: [...tableData]
        },
        table2: {
          columns: [...tableColumns],
          data: [...tableData]
        }
      }
    }
  }
</script>
<style>
</style>
