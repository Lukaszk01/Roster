{% extends "main/base.html" %}

{% block content %}
  <div class="mt-4" id="app">
    <div>[[ message ]]</div>
</div>
{{ username|json_script:"username" }}
  <div class="home-view-container">
    <h1>Add your info</h1>
      <h3>
        <font-awesome-icon icon="cat"/>
        {{ getAllCats.length }} +
        <font-awesome-icon icon="dog"/>
        {{ getAllDogs.length }}
      </h3>
    <button @click="togglePetForm" class="btn btn-primary">Add New Pet</button>

    <b-form @submit.prevent="handleSubmit" v-if="showForm">
      <b-form-group id="exampleInputGroup2" label="Pet's Name:" label-for="exampleInput2">
        <b-form-input
          id="exampleInput2"
          type="text"
          v-model="formData.name"
          required
          placeholder="Enter name" />
      </b-form-group>

      <b-form-group id="exampleInputGroup3" label="Species:" label-for="exampleInput3">
        <b-form-select id="exampleInput3" :options="['cats', 'dogs']" required v-model="formData.species" />
      </b-form-group>

      <b-form-group id="exampleInputGroup2" label="Pet's Age:" label-for="exampleInput2">
        <b-form-input
          id="exampleInput2"
          type="number"
          v-model="formData.age"
          required
          placeholder="Enter age" />
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
<script>
var username = JSON.parse(document.getElementById('username').textContent);
var app = new Vue({
  data() {
      return {
        showForm: false,
        formData: {
        name: '',
        age: 0,
        species: null
      },
      

  delimiters: ["[[", "]]"],
  el: '#app',
  data: {
    message: 'Elo elo 320 vue is working on this app mdf! ' + username
  },
  methods: {
    ...mapActions([
      'addPet'
    ]),
    togglePetForm () {
      this.showForm = !this.showForm
    },
};

</script>
<style scoped>

</style>
{% endblock %}