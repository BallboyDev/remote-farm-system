<script>
    import { onMount } from "svelte";
    import { Button, Input, InputGroup } from "@sveltestrap/sveltestrap";
    import { callApi } from "./api/callApi";

    let { loginStatus = $bindable() } = $props();

    let id = $state("");
    let loginSuccess = $state(false);

    onMount(() => {
        const userId = localStorage.getItem("userId");

        callApi("/api/user/login", "POST", { id: userId }).then((res) => {
            const { status, data } = res;

            if (status === "success") {
                id = data.id;
                loginStatus = true;
            }
        });
    });

    const handleLogin = () => {
        callApi("/api/user/login", "POST", { id }).then((res) => {
            const { status, data } = res;

            if (status === "success") {
                localStorage.setItem("userId", id);
                console.log(res);

                loginStatus = true;
            }
        });
    };

    const handleLogout = () => {
        localStorage.removeItem("userId");
        id = "";
        loginStatus = false;
    };
</script>

{#if !loginStatus}
    <div class="d-flex gap-2 justify-content-between w-100">
        <Input class="w-75" type="text" placeholder="아이디" bind:value={id} />
        <Button class="w-25" color="primary" onclick={handleLogin}
            >로그인</Button
        >
    </div>
{:else}
    <div class="d-flex gap-2 justify-content-between w-100">
        <Input class="w-75" type="text" disabled bind:value={id} />
        <Button class="w-25" color="primary" onclick={handleLogout}
            >로그아웃</Button
        >
    </div>
{/if}

<!-- A6042, B2772, C0546, D9364, E2282, admin-->
