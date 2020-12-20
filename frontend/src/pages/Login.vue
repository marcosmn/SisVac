<template>
  <div class="login">
    <div class="panel panel-default">
      <div class="panel-body">
        <div class="text-center">
          <div class="container">
            <div class="row">
              <div class="col">
                <div class=colorfundo>
                <h2>Acesso a conta</h2>
                <form class="form" ng-submit="login()">
                  <button
                      class="btn btn-lg btn-google"
                      type="submit">
                      <i class="fa fa-google fa-1x"></i> Login com o Google
                  </button>
                </form>
                </div>
              </div>
              
              <div class="col">
               <h2> Carteira digital de vacinação</h2>
                <h3>O que é? </h3>
                <p>A carteira digital de vacinação é uma plataforma online para os usuários do <b>Sistema Único de Saúde.</b></p>
                <p> Nela você pode <b>visualizar</b> seu <b>cartão de vacinação, realizar agendamento de vacinas</b> podendo escolher <b>local, data e hora</b> que deseja ser vacinado. </p>
                <h3>O que mais posso fazer?</h3>
                <p><b>Visualizar seu Cartão de Vacina</b></p>
                <p><b>Consultar sua posição na fila de espera da vacina</b></p>
                <p><b>Registrar a aplicação de vacinas de clínicas particulares</b></p>
              </div>
              
            </div>
          </div>
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
    background-color : white;
  }

  h2{
 
  color : rgba(13, 53, 113, 1);
  }

  h3{
  text-align:left;
  color : rgba(13, 53, 113, 1);
  }

  p{
    text-align:left;
  }

  div.login {


  }

</style>
