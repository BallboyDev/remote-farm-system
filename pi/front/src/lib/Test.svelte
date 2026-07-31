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
    <ButtonGroup>
        <Button
            color="primary"
            onclick={() => {
                test(4);
            }}>Test 4</Button
        >
        <Button
            color="warning"
            onclick={() => {
                test(5);
            }}>Test 5</Button
        >
        <Button
            color="danger"
            onclick={() => {
                test(6);
            }}>Test 6</Button
        >
    </ButtonGroup>
    <ButtonGroup>
        <Button
            color="primary"
            onclick={() => {
                test(7);
            }}>Test 7</Button
        >
        <Button
            color="warning"
            onclick={() => {
                test(8);
            }}>Test 8</Button
        >
        <Button
            color="danger"
            onclick={() => {
                test(9);
            }}>Test 9</Button
        >
    </ButtonGroup>
</WrapperModule>

<style>
</style>
