<template>
  <div class="login">
    <div class="panel panel-default">
      <div class="panel-body">
        <div class="text-center">
          <h1>Autenticação</h1>
          <form class="form" ng-submit="login()">
            <button
              class="btn btn-lg btn-google  btn-primary text-uppercase"
              type="submit"
            >
              <i class="fa fa-google fa-2x"></i> Login com o Google
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "login",
  data() {
    return {};
  },
  computed: mapState({
    logado: state => state.userState.logado,
    nome: state => state.userState.nome
  }),
  methods: mapActions('userState', [
    'getStatus'
  ]),
  created() {
    this.$store.dispatch('userState/getStatus')
  }
};
</script>

<style scoped>
  button.btn-google {
    background-color : red;
  }

</style>
