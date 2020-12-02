{% extends "main/base.html" %}
{% block content %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.2.3/velocity.min.js"></script>


<div id="components-demo">
  <button-counter></button-counter>
</div>
<script>
export default {
  Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
}
</script>
{{% endblock content %}}