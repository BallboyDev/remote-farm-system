<script lang="ts">
    import {
        Button,
        ButtonGroup,
        Input,
        InputGroup,
        InputGroupText,
    } from "@sveltestrap/sveltestrap";
    import WrapperModule from "./components/WrapperModule.svelte";
    import { callApi } from "./api/callApi";

    const test = (index: number) => {
        callApi(`/api/test/test${index}`, "GET").then((res) => {
            console.log(res);
        });
    };
</script>

<WrapperModule title="Test">
    <ButtonGroup>
        <Button
            color="primary"
            onclick={() => {
                test(1);
            }}>Test 1</Button
        >
        <Button
            color="warning"
            onclick={() => {
                test(2);
            }}>Test 2</Button
        >
        <Button
            color="danger"
            onclick={() => {
                test(3);
            }}>Test 3</Button
        >
    </ButtonGroup>
</WrapperModule>

<style>
</style>
