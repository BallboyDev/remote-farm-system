<script lang="ts">
  const login = false;

  const handleClick = () => {
    fetch("/api")
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
</script>

<div>
  {#if login}
    <button onclick={handleClick}>BTN1</button>
  {:else}
    <p>Please log in.</p>
  {/if}
</div>

<style>
  button {
    background-color: #4caf50;
    border: none;
    border-radius: 8px;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
</style>
