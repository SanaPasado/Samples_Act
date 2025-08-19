class FormUserMixin:
    def form_valid(self, form):
        # We assume the user is authenticated because of the LoginRequiredMixin
        form.instance.user = self.request.user
        return super().form_valid(form)


    #mixins parang for authentication lang tas formusermixin
    # para di na ilagay ulit ulit yung def form is valid function
