{% extends "main/base.html" %}

{% block content %}
  <div class="mt-4" id="app">
    <div>[[ message ]]</div>
</div>
{{ username|json_script:"username" }}
<div class="calculator">
<div class="display">{{ current }}</div>
</div?
<script>
var username = JSON.parse(document.getElementById('username').textContent);
var app = new Vue({
  data() {
      return {
        current: '',
        items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
      }
    },
  delimiters: ["[[", "]]"],
  el: '#app',
  data: {
    message: 'Elo elo 320 vue is working on this app mdf! ' + username
  },
});
</script>
<style scoped>
.display {
  grid-column: 1 / 5;
  background-color: #333;
  color: white;
}
.calculator {
  margin: 0 auto;
  width: 400px;
  font-size: 40px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(50px, auto);
}
</style>
{% endblock %}