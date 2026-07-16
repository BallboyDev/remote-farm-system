<script>
    import { onMount } from "svelte";
    import { Button, Input, InputGroup } from "@sveltestrap/sveltestrap";
    import { callApi } from "./api/callApi";

    let id = $state("");
    let loginSuccess = $state(false);

    onMount(() => {
        const storedId = localStorage.getItem("userId");
        if (storedId) {
            id = storedId;
            loginSuccess = true;
        }
    });

    const handleLogin = async () => {
        // 로그인 처리 로직을 여기에 작성합니다.
        const result = await callApi("/api/login", "POST", { id });
        const data = result.data;

        localStorage.setItem("userId", data.id);
        loginSuccess = true;
    };

    const handleLogout = () => {
        localStorage.removeItem("userId");
        loginSuccess = false;
        id = "";
    };
</script>

{#if !loginSuccess}
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
