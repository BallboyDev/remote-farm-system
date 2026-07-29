const open = () => {
    return { status: true, data: { message: "Gate opened" } };
}
const close = () => {
    return { status: true, data: { message: "Gate closed" } };
}

module.exports = {
    openGate: open,
    closeGate: close,
};  