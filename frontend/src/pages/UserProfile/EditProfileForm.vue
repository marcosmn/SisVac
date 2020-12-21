<template>
  <card>
    <h4 slot="header" class="card-title">Dados Pessoais</h4>
    <form>
      <div class="row">
        <div class="col-md-9">
          <base-input
            type="text"
            label="Nome"
            placeholder="Nome"
            v-model="user.nome"
          >
          </base-input>
        </div>
        <div class="col-md-3">
          <base-input
            type="text"
            label="Telefone"
            placeholder="Telefone"
            v-model="user.fone"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-6">
          <base-input
            type="text"
            label="CPF"
            placeholder="CPF"
            v-model="user.cpf"
          >
          </base-input>
        </div>
        <div class="col-md-6">
          <base-input
            type="text"
            label="Data Nascimento"
            placeholder="Data Nascimento"
            v-model="user.data_nascimento"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <base-input
            type="text"
            label="Endereço"
            placeholder="Home Endereço"
            v-model="user.endereco"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-4">
          <base-input
            type="text"
            label="Bairro"
            placeholder="Bairro"
            v-model="user.bairro"
          >
          </base-input>
        </div>
        <!--
        <div class="col-md-4">
          <base-input
            type="text"
            label="Cidade"
            placeholder="Cidade"
            v-model="user.cidade"
          >
          </base-input>
        </div>
        -->
        <div class="col-md-4">
          <base-input
            type="number"
            label="CEP"
            placeholder="ZIP Cep"
            v-model="user.cep"
          >
          </base-input>
        </div>
      </div>

      <div class="text-center">
        <button
          type="submit"
          class="btn btn-info btn-fill float-right"
          @click.prevent="updateProfile"
        >
          Salvar
        </button>
      </div>
      <div class="clearfix"></div>
    </form>
  </card>
</template>
<script>
import Card from "src/components/Cards/Card.vue";
import userService from "@/services/userService";

export default {
  components: {
    Card,
  },
  data() {
    return {
      user: {},
    };
  },
  mounted() {
    userService.getDados().then((dados) => {
        console.info(dados);
        this.user = dados;
    });
  },
  methods: {
    updateProfile() {
      userService.salvarDados(this.user);
      alert("Your data: " + JSON.stringify(this.user));

    },
  },
};
</script>
<style></style>
