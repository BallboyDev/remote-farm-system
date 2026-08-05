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
    <Input placeholder="Test Input" type="text" />
    <ButtonGroup>
        <Button
            color="primary"
            onclick={() => {
                test(1);
            }}>1 : led / on</Button
        >
        <Button
            color="warning"
            onclick={() => {
                test(2);
            }}>2 : led / off</Button
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
            color="secondary"
            onclick={() => {
                test(4);
            }}>4 : ir / transmit</Button
        >
        <Button
            color="success"
            onclick={() => {
                test(5);
            }}>5 : ir / test</Button
        >
        <Button
            color="info"
            onclick={() => {
                test(6);
            }}>Test 6</Button
        >
    </ButtonGroup>
    <ButtonGroup>
        <Button
            color="light"
            onclick={() => {
                test(7);
            }}>Test 7</Button
        >
        <Button
            color="dark"
            onclick={() => {
                test(8);
            }}>Test 8</Button
        >
        <Button
            color="primary"
            outline
            onclick={() => {
                test(9);
            }}>Test 9</Button
        >
    </ButtonGroup>
</WrapperModule>

<style>
</style>
