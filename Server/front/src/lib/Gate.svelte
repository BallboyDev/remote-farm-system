<script lang="ts">
    import {
        Button,
        Input,
        InputGroup,
        InputGroupText,
    } from "@sveltestrap/sveltestrap";
    import WrapperModule from "./components/WrapperModule.svelte";
    import { callApi } from "./api/callApi";

    let state = $state(0); // 0: close, 1: open

    const handleOpen = async () => {
        const result = await callApi("/api/gate/open", "GET");
        console.log(result);
    };

    const handleClose = async () => {
        const result = await callApi("/api/gate/close", "GET");
        console.log(result);
    };
</script>

<WrapperModule title="Gate" {state}>
    <Button color="primary" disabled>OPEN</Button>

    <div class="d-flex gap-2 justify-content-between">
        <Button color="primary" outline class="w-100" onclick={handleOpen}
            >OPEN</Button
        >
        <Button color="danger" outline class="w-100" onclick={handleOpen}
            >CLOSE</Button
        >
    </div>
</WrapperModule>

<style>
</style>
