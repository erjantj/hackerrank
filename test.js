this.campaignService.createCampaign(this.newCampaign, this.trixUrl)
        .then((msg) => {
            // Campaign was created successfully.
            const cam = msg.getCampaign();

            const numValid = msg.getNumValid();
            const userMsg =
                `Successfully created campaign. ${numValid} users were added`;
            this.mdDialog.show(this.mdDialog.alert()
                                   .title('Successfully created campaign')
                                   .textContent(userMsg)
                                   .ok('Ok'));

            // Clear the selected campaign and redirect to the edit tab.
            this.campaignService.campaign = null;
            this.state_.go('campaign.edit', {campaignId: cam.getId()});
        })
        .catch(({errorMsg, details}) => {
            let message = errorMsg.getMessage();

            if (errorMsg.getStatus() === Code.INVALID_ARGUMENT) {
               if (details.invalidUsers) {
                // There are some invalid users in the trix.
                this.showInvalidUsersDialog(details.invalidUsers);
                return;
              }
              form.serverError = details;
          }

          message = `Failed to create campaign. ${message}`;
          this.mdDialog.show(this.mdDialog.alert()
                                 .title('There was a problem')
                                 .ariaLabel('Error notification')
                                 .textContent(message)
                                 .ok('Ok'));
        });