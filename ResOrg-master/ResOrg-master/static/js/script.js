function redirect_signin(){
    location.href = "/signin";
}

function redirect_signup(){
    location.href = "/signup";
}

function redirect_logout(){
    window.location.href = "/signout";
}

function redirect_profile(){
    location.href = "profile";
}

function redirect_dashboard(){
    location.href = "/dashboard";
}

function redirect_topic(id){
    location.href = "topic/" + id + "/";
}

function animate_header(){
    let header = document.getElementById("hero-nav");
    let height = header.offsetHeight;
    
    if( window.scrollY > height )  
        header.classList.add("sticky");
    else
        header.classList.remove("sticky");
    
    if( window.scrollY > (height*3) )
        header.classList.add("animate-header");
    else
        header.classList.remove("animate-header");
}

function add_popup_events(pop, bg){
    pop.style.display = "flex";
    bg.style.pointerEvents = "none";
    bg.classList.add("blurdiv");
    document.body.style.overflow = "hidden";
}

function remove_popup_events(pop, bg){
    pop.style.display = "none";
    bg.style.pointerEvents = "all";
    bg.classList.remove("blurdiv");
    document.body.style.overflow = "auto";
}

function open_group_dialog(){
    let pop = document.getElementById("group-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
    document.getElementById('group-dialog-id').classList.add('show');
}

function close_group_dialog(){
    let pop = document.getElementById("group-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_topic_dialog(){
    let pop = document.getElementById("topic-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_topic_dialog(){
    let pop = document.getElementById("topic-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_logout_dialog(){
    let pop = document.getElementById("logout-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_logout_dialog(){
    let pop = document.getElementById("logout-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
    if( document.getElementById("nav-account").style.width == "300px" ) open_account_sidenav();
}

function open_editprofile_dialog(){
    let pop = document.getElementById("editprofile-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_editprofile_dialog(){
    let pop = document.getElementById("editprofile-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
    if( document.getElementById("nav-account").style.width == "300px" ) open_account_sidenav();
}

function open_changepassword_dialog(){
    let pop = document.getElementById("changepassword-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_changepassword_dialog(){
    let pop = document.getElementById("changepassword-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
    if( document.getElementById("nav-account").style.width == "300px" ) open_account_sidenav();
}

function open_createtodo_dialog(){
    let pop = document.getElementById("createtodo-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_createtodo_dialog(){
    let pop = document.getElementById("createtodo-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_edittodo_dialog(){
    let pop = document.getElementById("edittodo-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_edittodo_dialog(){
    let pop = document.getElementById("edittodo-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_renamegroup_dialog(){
    let pop = document.getElementById("renamegroup-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_renamegroup_dialog(){
    let pop = document.getElementById("renamegroup-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_deletegroup_dialog(){
    let pop = document.getElementById("deletegroup-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_deletegroup_dialog(){
    let pop = document.getElementById("deletegroup-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_renametopic_dialog(){
    let pop = document.getElementById("renametopic-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_renametopic_dialog(){
    let pop = document.getElementById("renametopic-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_deletetopic_dialog(){
    let pop = document.getElementById("deletetopic-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_deletetopic_dialog(){
    let pop = document.getElementById("deletetopic-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_delete_account_dialog(){
    let pop = document.getElementById("deleteaccount-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_delete_account_dialog(){
    let pop = document.getElementById("deleteaccount-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_account_sidenav(){
    document.getElementById("nav-account").style.width = "300px";
    let bg = document.getElementById("dashface");
    bg.style.pointerEvents = "none";
    bg.classList.add("blurdiv");
    document.body.style.overflow = "hidden";
}

function close_account_sidenav(){
    document.getElementById("nav-account").style.width = "0";
    let bg = document.getElementById("dashface");
    bg.style.pointerEvents = "all";
    bg.classList.remove("blurdiv");
    document.body.style.overflow = "auto";
}

function show_account_dropdown() {
    document.getElementById("dropdown-account-id").classList.toggle("account-dropdown-show");
}

window.onclick = function(e){
    if(!e.target.matches('.dropbtn')){
        var account_dropdown = document.getElementById("dropdown-account-id");
        if( account_dropdown != null && account_dropdown.classList.contains('account-dropdown-show')){
            account_dropdown.classList.remove('account-dropdown-show');
        }
        
        var add_menu_drodown = document.getElementById("dropdown-add-menu-id");
        if( add_menu_drodown != null && add_menu_drodown.classList.contains('add-menu-dropdown-show')){
            add_menu_drodown.classList.remove('add-menu-dropdown-show');
        }

        var group_menu_drodown = document.getElementById("dropdown-group-menu-id");
        if( group_menu_drodown != null && group_menu_drodown.classList.contains('group-menu-dropdown-show')){
            group_menu_drodown.classList.remove('group-menu-dropdown-show');
        }

        var sort_menu_drodown = document.getElementById("dropdown-sort-menu-id");
        if( sort_menu_drodown != null && sort_menu_drodown.classList.contains('sort-menu-dropdown-show')){
            sort_menu_drodown.classList.remove('sort-menu-dropdown-show');
        }
    }
}

function enable_editmode(){
    let textarea = document.getElementById('note-write-area');
    if( textarea.disabled ){
        document.getElementById('note-button').innerHTML = "Save <img class=\"feature-icon\" src=\"media/sidebar-feature/save.png\">";
        textarea.disabled = false;
    }
    else{
        document.getElementById('note-button').innerHTML = "Edit <img class=\"feature-icon\" src=\"media/sidebar-feature/edit.png\">";
        textarea.disabled = true;
    }
    textarea.focus();
}

function toggle_darkmode(){
    
}

function auto_grow(element){
    element.style.height = "5px";
    element.style.height = (element.scrollHeight) + "px";
}

function show_add_menu_dropdown() {
    document.getElementById("dropdown-add-menu-id").classList.toggle("add-menu-dropdown-show");
}

function show_group_menu_dropdown() {
    document.getElementById("dropdown-group-menu-id").classList.toggle("group-menu-dropdown-show");
}

function show_sort_menu_dropdown() {
    document.getElementById("dropdown-sort-menu-id").classList.toggle("sort-menu-dropdown-show");
}

function open_renameitem_dialog(){
    let pop = document.getElementById("renameitem-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_renameitem_dialog(){
    let pop = document.getElementById("renameitem-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_deleteitem_dialog(){
    let pop = document.getElementById("deleteitem-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_deleteitem_dialog(){
    let pop = document.getElementById("deleteitem-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}


// TOPIC UTILS - START
function open_addweblink_dialog(){
    let pop = document.getElementById("addweblink-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_addweblink_dialog(){
    let pop = document.getElementById("addweblink-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_addytlink_dialog(){
    let pop = document.getElementById("addytlink-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
}

function close_addytlink_dialog(){
    let pop = document.getElementById("addytlink-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

function open_section_dialog(){
    let pop = document.getElementById("section-dialog-id");
    let bg = document.getElementById("dashface");
    add_popup_events(pop, bg);
    document.getElementById('section-dialog-id').classList.add('show');
}

function close_section_dialog(){
    let pop = document.getElementById("section-dialog-id");
    let bg = document.getElementById("dashface");
    remove_popup_events(pop, bg);
}

// TOPIC UTILS - END

// 
function redirect_back(){
    window.location.href = "./";
}
function redirect_home(){
    location.href = "/";
}
function open_popup(id_name){
    document.getElementById(id_name).classList.toggle("hide");
}
function close_popup(id_name){
    document.getElementById(id_name).classList.toggle("hide");    
}
// 