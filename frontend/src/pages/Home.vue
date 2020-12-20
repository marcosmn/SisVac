<template>
  <div class="login">
    <div class="panel panel-default">
      <div class="panel-body">
        <div class="text-center">
          <div class="container">
            <div class="col">
              <h2>Carteira digital de vacinação</h2>
              <h3>O que é?</h3>
              <p>
                A carteira digital de vacinação é uma plataforma online para os
                usuários do <b>Sistema Único de Saúde.</b>
              </p>
              <p>
                Nela você pode <b>visualizar</b> seu
                <b>cartão de vacinação, realizar agendamento de vacinas</b>
                podendo escolher <b>local, data e hora</b> que deseja ser
                vacinado.
              </p>
              <h3>O que mais posso fazer?</h3>
              <p><b>Visualizar seu Cartão de Vacina</b></p>
              <p><b>Consultar sua posição na fila de espera da vacina</b></p>
              <p>
                <b>Registrar a aplicação de vacinas de clínicas particulares</b>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {};
  },
};
</script>

<style scoped>
button.btn-google {
  background-color: white;
}

h2 {
  color: rgba(13, 53, 113, 1);
}

h3 {
  text-align: left;
  color: rgba(13, 53, 113, 1);
}

p {
  text-align: left;
}

</style>
