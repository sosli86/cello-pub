pragma solidity >=0.7.0;

// @ Record of contact between two or more individuals.
contract Contact {

    // Represents a single User.
    struct User {
        address user_address;
        string user_name;
    }

    // Dynamic array of Users.
    User[] user_list;

    // Map of users keyed by their addresses.
    mapping(address => User) user_map;

    // Represents a single message sent by any contactee.
    struct Message {
        address contract_address;
        uint message_number;
        User message_sender;
        string message_content;
    }

    uint message_count= 0;

    // Dynamically sized array of "Message" structs.
    Message[] message_archive;

    // Adds a new User to the contract.
    function addUser(string calldata newContacteeName) external returns (User[] memory) {
        user_list.push(User({user_address: msg.sender, user_name: newContacteeName}));
        return user_list;
    }

    // Adds a new Message to the contract.
    function addMessage(string memory new_message_sender_name, string calldata new_message_content) external returns (Message[] memory) {
        message_count += 1;
        Message memory new_message = Message({contract_address: address(this), message_number: message_count, message_sender: User({user_address: msg.sender, user_name: new_message_sender_name}), message_content: new_message_content});
        message_archive.push(new_message);
        return getMessageArchive();
    }

    // Message archive getter.
    function getMessageArchive() private view returns (Message[] memory) {
        return message_archive;
    }

    // User list getter.
    function getUserList() private view returns (User[] memory) {
        return user_list;
    }
}
