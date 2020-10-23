{% extends "main/base.html" %}
{% block content %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.2.3/velocity.min.js"></script>


<div id="example-3">
  <button v-on:click="say('hi')">Say hi</button>
  <button v-on:click="say('what')">Say what</button>
</div>

<script>
new Vue({
  el: '#example-3',
  methods: {
    say: function (message) {
      alert(message)
    }
  }
})
  
}
</script>
</script>
<style scoped>
  #staggered-list-demo {
    color: pink;

}
</style>
{% endblock %}