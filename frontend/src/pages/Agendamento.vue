<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <agendamento-form>
          </agendamento-form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import AgendamentoForm from './Agendamento/AgendamentoForm.vue'

  export default {
    components: {
      AgendamentoForm,
    }
  }

</script>
<style>

</style>
