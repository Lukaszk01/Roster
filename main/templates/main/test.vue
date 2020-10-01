{% extends "main/base.html" %}

{% block content %}
  <div class="mt-4" id="app">
    <div>[[ message ]]</div>
</div>
{{ username|json_script:"username" }} 





<script>
var username = JSON.parse(document.getElementById('username').textContent);
var app = new Vue({
  data() {
      return {
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
{% endblock %}